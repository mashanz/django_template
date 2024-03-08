let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = { allowUnfree = true; }; overlays = []; };

  git = pkgs.git.overrideAttrs (oldAttrs: rec {
    version = "2.42.0";
  });

  podman = pkgs.podman.overrideAttrs (oldAttrs: rec {
    version = "4.7.2";
  });

  postgresql = pkgs.postgresql_15.overrideAttrs (oldAttrs: rec {
    version = "15.4";
  });
in

pkgs.mkShell {
  packages = with pkgs; [
    git
    poetry
    podman
    nodejs_20
    python312
    pkgs.pdm
    redis
    pkgs.postgresql
    unzip
  ];

  shellHook = ''
    alias docker=podman
    export NIX_SHELL_DIR=$PWD/.nix-shell
    export LC_ALL=C
    export LANG=C.utf8

    export PGDATA=$NIX_SHELL_DIR/db
    export PGHOST=localhost
    export PGUSER=postgres
    export PGPASSWORD=password

    # Setup PostgreSQL
    mkdir $NIX_SHELL_DIR
    
   trap \
    "
      pg_ctl -D $PGDATA stop
      pkill redis-server
    " \
    EXIT

    if ! test -d $PGDATA
    then
      initdb -D $PGDATA --no-locale --encoding=UTF8
    fi

    HOST_COMMON="host\s\+all\s\+all"
    sed -i "s|^$HOST_COMMON.*127.*$|host all all 0.0.0.0/0 trust|" $PGDATA/pg_hba.conf
    sed -i "s|^$HOST_COMMON.*::1.*$|host all all ::/0 trust|"      $PGDATA/pg_hba.conf

    pg_ctl                                                  \
      -D $PGDATA                                            \
      -l $PGDATA/postgres.log                               \
      -o "-c unix_socket_directories='$PGDATA'"             \
      -o "-c listen_addresses='*'"                          \
      -o "-c log_destination='stderr'"                      \
      -o "-c logging_collector=on"                          \
      -o "-c log_directory='log'"                           \
      -o "-c log_filename='postgresql-%Y-%m-%d_%H%M%S.log'" \
      -o "-c log_min_messages=info"                         \
      -o "-c log_min_error_statement=info"                  \
      -o "-c log_connections=on"                            \
      start

    echo "Setup database.. To access DB: psql -U $PGUSER -d postgres"
    if ! psql -U $(whoami) -tAc "SELECT 1 FROM pg_database WHERE datname='development'" | grep -q 1; then
      createuser -U $(whoami)
      psql -U $(whoami) -d postgres -c "CREATE DATABASE $(whoami) OWNER $(whoami);" || true
      psql -U $(whoami) -d postgres -c "ALTER ROLE $PGUSER SUPERUSER;"
      psql -U "$PGUSER" -d postgres -c "CREATE DATABASE development" || true
    fi

    if ! command -v bun &> /dev/null; then
      echo "Installing bun..."
      curl -fsSL https://bun.sh/install | bash
    fi

    echo "Run redis.. See log on $NIX_SHELL_DIR/redis.log"
    nohup redis-server > $NIX_SHELL_DIR/redis.log 2>&1 &
  '';
}