from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[194.541958,8.809667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_125810.07+084834.8/sdB_SDSSJ910_125810.07+084834.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_125810.07+084834.8/sdB_SDSSJ910_125810.07+084834.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
