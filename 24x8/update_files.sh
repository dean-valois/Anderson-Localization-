echo "Copying eigenvalue files from Bielefeld cluster"

rsync -r --size-only --include="eigL*" --include="COMPLETE" --include="*/" --exclude="*" -v influx:/work/DATA/dvalois/database/anderson_transition/24x8/* ./
