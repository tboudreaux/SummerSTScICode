from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[348.1555,42.453103],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j23126+4227/sdB_galex_j23126+4227_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j23126+4227/sdB_galex_j23126+4227_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
