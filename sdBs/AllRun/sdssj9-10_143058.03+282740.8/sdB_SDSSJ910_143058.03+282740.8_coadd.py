from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.741792,28.461333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_143058.03+282740.8/sdB_SDSSJ910_143058.03+282740.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_143058.03+282740.8/sdB_SDSSJ910_143058.03+282740.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
