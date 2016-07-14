from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[358.401417,-36.505289],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_2351-3647/sdB_MCT_2351-3647_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_2351-3647/sdB_MCT_2351-3647_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
