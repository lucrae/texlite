while true; do
    read -p "Have you updated __version__ in texlite/_version.py? " answer
    case $answer in
        [Yy]* ) break;;
        [Nn]* ) echo "Please do that.";;
        * ) echo "Please answer yes or no.";;
    esac
done