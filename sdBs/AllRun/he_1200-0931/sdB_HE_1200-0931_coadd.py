from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[180.840667,-9.801831],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_1200-0931/sdB_HE_1200-0931_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_1200-0931/sdB_HE_1200-0931_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
