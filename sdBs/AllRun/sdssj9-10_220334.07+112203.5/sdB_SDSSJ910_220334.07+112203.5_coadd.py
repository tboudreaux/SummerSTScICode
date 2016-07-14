from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[330.891958,11.367639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_220334.07+112203.5/sdB_SDSSJ910_220334.07+112203.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_220334.07+112203.5/sdB_SDSSJ910_220334.07+112203.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
