from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[310.014667,-24.025617],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BPS_CS22955-176/sdB_BPS_CS22955-176_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BPS_CS22955-176/sdB_BPS_CS22955-176_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
