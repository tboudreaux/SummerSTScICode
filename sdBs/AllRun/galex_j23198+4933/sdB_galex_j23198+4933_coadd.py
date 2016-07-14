from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.953917,49.565797],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j23198+4933/sdB_galex_j23198+4933_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j23198+4933/sdB_galex_j23198+4933_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
