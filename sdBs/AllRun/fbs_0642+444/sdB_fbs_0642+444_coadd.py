from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[101.607125,44.356333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0642+444/sdB_fbs_0642+444_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0642+444/sdB_fbs_0642+444_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
