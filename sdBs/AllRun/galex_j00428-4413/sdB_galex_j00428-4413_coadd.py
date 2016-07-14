from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.701375,-44.22335],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j00428-4413/sdB_galex_j00428-4413_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j00428-4413/sdB_galex_j00428-4413_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
