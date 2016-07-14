from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[205.345667,3.297694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_134122.96+031751.7/sdB_sdssj_134122.96+031751.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_134122.96+031751.7/sdB_sdssj_134122.96+031751.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
