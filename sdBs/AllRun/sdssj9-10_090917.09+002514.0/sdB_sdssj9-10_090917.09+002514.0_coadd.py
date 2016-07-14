from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[137.321208,0.420556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_090917.09+002514.0/sdB_sdssj9-10_090917.09+002514.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_090917.09+002514.0/sdB_sdssj9-10_090917.09+002514.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
