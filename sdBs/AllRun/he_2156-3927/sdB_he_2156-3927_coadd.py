from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.897917,-39.220778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_2156-3927/sdB_he_2156-3927_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_2156-3927/sdB_he_2156-3927_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
