#!/usr/local/bin/bash -l

source /global/etc/sh.bashrc

module unload msip_shell_sch_utils
module unload msip_shell_lay_utils
module unload msip_shell_rename
module unload python
module unload msip_hipre_lib_utils
module unload lc
module unload msip_shell_dotlib_utils
module unload msip_cad_env
module unload msip_shared_lib

module load msip_shell_sch_utils
module load msip_shell_lay_utils
module load msip_shell_rename
module load python
module load msip_hipre_lib_utils
module load lc
module load msip_shell_dotlib_utils
module load msip_cad_env
module load msip_shared_lib


python main.py
