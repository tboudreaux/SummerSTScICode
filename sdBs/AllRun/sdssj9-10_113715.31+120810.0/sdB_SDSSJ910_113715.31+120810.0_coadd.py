from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.313792,12.136111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_113715.31+120810.0/sdB_SDSSJ910_113715.31+120810.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_113715.31+120810.0/sdB_SDSSJ910_113715.31+120810.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
