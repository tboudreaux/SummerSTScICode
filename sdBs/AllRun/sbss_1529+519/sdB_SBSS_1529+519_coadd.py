from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[232.752167,51.752056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1529+519/sdB_SBSS_1529+519_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1529+519/sdB_SBSS_1529+519_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
