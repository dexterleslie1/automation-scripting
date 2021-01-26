import cli_common
import os


class GrafanaCli(object):
    """
    Cli for managing grafana. OS support: centOS8
    """

    def install(self):
        """
        Install grafana.

        :return:
        """

        # Full path of python file locates in
        var_full_path = os.path.dirname(os.path.realpath(__file__))

        var_install = raw_input("Install grafana? [y/n]: ")
        if var_install.lower() == "y":
            var_host_prometheus = raw_input("Enter target machine of deploying grafana (example: 192.168.1.20:8080): ")
            var_host_prometheus_user = raw_input("Enter target machine user (default root): ") or "root"

        # Install grafana
        if var_install.lower() == "y":
            var_command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook " + var_full_path + "/role_grafana_install.yml"
            var_command = cli_common.concat_command(var_command, var_host_prometheus, var_host_prometheus_user)
            cli_common.execute_command(var_command)