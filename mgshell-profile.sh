function ns() { 
    cd $(/usr/libexec/mgshell/ns $1)
}

function pod() { 
    cd $(/usr/libexec/mgshell/pod $1)
}

function log() { 
    /usr/libexec/mgshell/log $1
}

function root() { 
    cd $(/usr/libexec/mgshell/root $1)
}
