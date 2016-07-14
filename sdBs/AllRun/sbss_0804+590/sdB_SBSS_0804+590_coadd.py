from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.081792,58.873028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_0804+590/sdB_SBSS_0804+590_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_0804+590/sdB_SBSS_0804+590_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
