from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[223.949083,10.012444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_J145547.78+100044.8/sdB_SDSSJ910_J145547.78+100044.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_J145547.78+100044.8/sdB_SDSSJ910_J145547.78+100044.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
