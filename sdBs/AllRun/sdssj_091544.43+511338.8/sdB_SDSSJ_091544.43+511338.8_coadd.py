from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.935125,51.227444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_091544.43+511338.8/sdB_SDSSJ_091544.43+511338.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_091544.43+511338.8/sdB_SDSSJ_091544.43+511338.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
