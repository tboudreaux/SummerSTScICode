from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[162.576583,-27.510283],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j10503-2730/sdB_galex_j10503-2730_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j10503-2730/sdB_galex_j10503-2730_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
