# downloads


========================================================
- .bashrc

# Enable the subsequent settings only in interactive sessions
case $- in
  *i*) ;;
    *) return;;
esac

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User specific environment
#if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
PATH="$HOME/.local/bin:$HOME/bin:$PATH"
#fi
export PATH

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
    for rc in ~/.bashrc.d/*; do
        if [ -f "$rc" ]; then
            . "$rc"
        fi
    done
fi
unset rc

mkcdir ()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}

export TERM=xterm-256color
export COLORTERM=24bit

if [ ! -z "$TERMCAP" ] && [ "$TERM" == "screen" ]; then                         
    export TERMCAP=$(echo $TERMCAP | sed -e 's/Co#8/Co#256/g')                  
fi

alias vi=nvim
alias vim=nvim
alias fats='cd ~/work/cpp/fats2'
alias logs='cd /var/fats/logs'
alias data='cd /var/fats/data'
alias dump='cd /var/fats/dump'
alias monitoring='cd /var/fats/monitoring/'
alias diff=colordiff
alias far='far2l --tty;'

export FILTER_BRANCH_SQUELCH_WARNING=1
export GIT_TEST_DISALLOW_ABBREVIATED_OPTIONS=false

ulimit -c unlimited
ulimit -S -c unlimited > /dev/null 2>&1

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi

PATH=$PATH:/opt/SMathStudio:/opt/java/async-profiler/latest/bin:/opt/java/maven/latest/bin:/opt/java/gradle/latest/bin:/home/kav/.local/bin:~/.npm-global/bin
export PATH

export CLAUDE_CODE_MAX_OUTPUT_TOKENS=100000

# PyTorch + ROCm
#export HSA_OVERRIDE_GFX_VERSION=10.3.0
#export HIP_VISIBLE_DEVICES=0

red="\[$(tput setaf 1)\]"
green="\[$(tput setaf 2)\]"
blue="\[$(tput setaf 4)\]"
white="\[$(tput setaf 7)\]"
yellow="\[$(tput setaf 3)\]"
magenta="\[$(tput setaf 5)\]"
cyan="\[$(tput setaf 6)\]"
reset="\[$(tput sgr0)\]"
bold="\[$(tput bold)\]"

#export PS1="${bold}${cyan}\u${reset}:${green}\w${reset}\$ "

export THEME_CHECK_SUDO=false
export POWERLINE_COMPACT=1
export POWERLINE_PROMPT_USER_INFO_MODE=""

# Path to your oh-my-bash installation.
export OSH='/home/kav/.oh-my-bash'

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-bash is loaded.
OSH_THEME="powerline"

# If you set OSH_THEME to "random", you can ignore themes you don't like.
# OMB_THEME_RANDOM_IGNORED=("powerbash10k" "wanelo")

# Uncomment the following line to use case-sensitive completion.
# OMB_CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# OMB_HYPHEN_SENSITIVE="false"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_OSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you don't want the repository to be considered dirty
# if there are untracked files.
# SCM_GIT_DISABLE_UNTRACKED_DIRTY="true"

# Uncomment the following line if you want to completely ignore the presence
# of untracked files in the repository.
# SCM_GIT_IGNORE_UNTRACKED="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.  One of the following values can
# be used to specify the timestamp format.
# * 'mm/dd/yyyy'     # mm/dd/yyyy + time
# * 'dd.mm.yyyy'     # dd.mm.yyyy + time
# * 'yyyy-mm-dd'     # yyyy-mm-dd + time
# * '[mm/dd/yyyy]'   # [mm/dd/yyyy] + [time] with colors
# * '[dd.mm.yyyy]'   # [dd.mm.yyyy] + [time] with colors
# * '[yyyy-mm-dd]'   # [yyyy-mm-dd] + [time] with colors
# If not set, the default value is 'yyyy-mm-dd'.
# HIST_STAMPS='yyyy-mm-dd'

# Uncomment the following line if you do not want OMB to overwrite the existing
# aliases by the default OMB aliases defined in lib/*.sh
# OMB_DEFAULT_ALIASES="check"

# Would you like to use another custom folder than $OSH/custom?
# OSH_CUSTOM=/path/to/new-custom-folder

# To disable the uses of "sudo" by oh-my-bash, please set "false" to
# this variable.  The default behavior for the empty value is "true".
OMB_USE_SUDO=false

# To enable/disable display of Python virtualenv and condaenv
# OMB_PROMPT_SHOW_PYTHON_VENV=true  # enable
# OMB_PROMPT_SHOW_PYTHON_VENV=false # disable

# To enable/disable Spack environment information
# OMB_PROMPT_SHOW_SPACK_ENV=true  # enable
# OMB_PROMPT_SHOW_SPACK_ENV=false # disable

# Which completions would you like to load? (completions can be found in ~/.oh-my-bash/completions/*)
# Custom completions may be added to ~/.oh-my-bash/custom/completions/
# Example format: completions=(ssh git bundler gem pip pip3)
# Add wisely, as too many completions slow down shell startup.
completions=(
  git
  composer
  ssh
)

# Which aliases would you like to load? (aliases can be found in ~/.oh-my-bash/aliases/*)
# Custom aliases may be added to ~/.oh-my-bash/custom/aliases/
# Example format: aliases=(vagrant composer git-avh)
# Add wisely, as too many aliases slow down shell startup.
aliases=(
  general
)

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-bash/plugins/*)
# Custom plugins may be added to ~/.oh-my-bash/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  bashmarks
)

# Which plugins would you like to conditionally load? (plugins can be found in ~/.oh-my-bash/plugins/*)
# Custom plugins may be added to ~/.oh-my-bash/custom/plugins/
# Example format:
#  if [ "$DISPLAY" ] || [ "$SSH" ]; then
#      plugins+=(tmux-autoattach)
#  fi

# Define colors
source "$OSH"/oh-my-bash.sh

# User configuration
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-bash libs,
# plugins, and themes. Aliases can be placed here, though oh-my-bash
# users are encouraged to define aliases within the OSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias bashconfig="mate ~/.bashrc"
# alias ohmybash="mate ~/.oh-my-bash"
#
# Define colors
#
# Override the prompt color for sudo (root)

export STM32_PRG_PATH=/opt/ST/STM32CubeProgrammer/bin

# Questa*-Intel® FPGA Starter Edition SW-QUESTA License file
export LM_LICENSE_FILE=/home/kav/.intel/licenses/LR-263887_License.dat
export SALT_LICENSE_SERVER=/home/kav/.intel/licenses/LR-263887_License.dat
export MGLS_LICENSE_FILE=/home/kav/.intel/licenses/LR-263887_License.dat
#export LM_LICENSE_FILE=~/.intel/licenses/lic_qsim_24_my.dat
export PATH=/opt/altera/latest/quartus/bin:/opt/altera/latest/questa_fse/bin:$PATH:
# Set Questa/Modelsim environment variables
export MODEL_TECH="/opt/altera/latest/questa_fse/bin"
export QUESTA_HOME="/opt/altera/latest/questa_fse"

# Vivado
export PATH="/opt/Xilinx/latest/Vivado/bin:$PATH"

# Verible (SystemVerilog parsing)
export PATH="/opt/verible/latest/bin:$PATH"

# Claude
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=75

# SystemVerilog language server (https://github.com/dalance/svls)
export PATH="/opt/svlint/latest/bin:/opt/svls/latest:$PATH"

export QSYS_ROOTDIR="/opt/altera/25.3/qsys/bin"

# Added by Quartus Prime software
#export SALT_LICENSE_FILE="/home/kav/.altera.quartus/questa_lic.dat"

# Add slang
export PATH="/opt/slang/latest/bin:$PATH"

# Add slang-server
export PATH="/opt/slang-server/latest/bin:$PATH"

========================================================
- .vimrc

set t_Co=256                                                                

set nocompatible              " be iMproved, required
filetype off                  " required

" You might have to force true color when using regular vim inside tmux as the
" colorscheme can appear to be grayscale with "termguicolors" option enabled.
if !has('gui_running') && &term =~ '^\%(screen\|tmux\)'
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
endif
syntax on
set termguicolors

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
