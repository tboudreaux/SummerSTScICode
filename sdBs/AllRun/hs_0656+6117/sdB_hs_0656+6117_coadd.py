from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.140917,61.220339],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_0656+6117/sdB_hs_0656+6117_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_0656+6117/sdB_hs_0656+6117_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
