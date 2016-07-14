from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[27.729708,2.877639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lamost_j015055.13+025239.5/sdB_lamost_j015055.13+025239.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lamost_j015055.13+025239.5/sdB_lamost_j015055.13+025239.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
