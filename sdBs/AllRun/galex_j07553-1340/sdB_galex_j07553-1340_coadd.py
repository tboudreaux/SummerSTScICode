from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[118.843167,-13.675442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j07553-1340/sdB_galex_j07553-1340_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j07553-1340/sdB_galex_j07553-1340_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
