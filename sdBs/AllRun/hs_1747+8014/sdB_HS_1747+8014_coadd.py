from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.788792,80.217881],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1747+8014/sdB_HS_1747+8014_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1747+8014/sdB_HS_1747+8014_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
