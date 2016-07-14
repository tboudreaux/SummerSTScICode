from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.176625,5.994222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_155642.39+055939.2/sdB_SDSSJ910_155642.39+055939.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_155642.39+055939.2/sdB_SDSSJ910_155642.39+055939.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
