from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[358.150417,-30.169192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_2350-3026/sdB_MCT_2350-3026_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_2350-3026/sdB_MCT_2350-3026_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
