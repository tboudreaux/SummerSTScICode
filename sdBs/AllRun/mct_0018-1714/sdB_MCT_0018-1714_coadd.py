from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[5.343542,-16.963417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0018-1714/sdB_MCT_0018-1714_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0018-1714/sdB_MCT_0018-1714_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
