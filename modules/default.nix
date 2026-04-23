{ inputs, ... }:
{
  systems = [
    "x86_64-linux"
  ];

  perSystem =
    {
      config,
      pkgs,
      ...
    }:
    {

      devShells.default = pkgs.mkShell {

        packages = [
          # add packages to use in shell
          pkgs.python3
        ];
      };
    };
}
