from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.642042,27.361056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_173034.09+272139.8/sdB_SDSSJ_173034.09+272139.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_173034.09+272139.8/sdB_SDSSJ_173034.09+272139.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
