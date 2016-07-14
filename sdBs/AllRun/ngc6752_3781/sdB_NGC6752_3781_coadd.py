from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.874292,-60.048497],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_NGC6752_3781/sdB_NGC6752_3781_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_NGC6752_3781/sdB_NGC6752_3781_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
