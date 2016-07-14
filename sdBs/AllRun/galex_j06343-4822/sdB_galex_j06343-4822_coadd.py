from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[98.597375,-48.368714],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j06343-4822/sdB_galex_j06343-4822_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j06343-4822/sdB_galex_j06343-4822_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
