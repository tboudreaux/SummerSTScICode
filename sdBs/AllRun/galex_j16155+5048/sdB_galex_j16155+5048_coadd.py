from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.88925,50.807131],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j16155+5048/sdB_galex_j16155+5048_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j16155+5048/sdB_galex_j16155+5048_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
