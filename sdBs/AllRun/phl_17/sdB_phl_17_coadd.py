from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[322.666125,-3.062056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_phl_17/sdB_phl_17_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_phl_17/sdB_phl_17_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
