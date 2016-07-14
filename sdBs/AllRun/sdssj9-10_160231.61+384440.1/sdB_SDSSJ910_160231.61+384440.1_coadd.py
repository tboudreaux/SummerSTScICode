from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.631708,38.744472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_160231.61+384440.1/sdB_SDSSJ910_160231.61+384440.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_160231.61+384440.1/sdB_SDSSJ910_160231.61+384440.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
