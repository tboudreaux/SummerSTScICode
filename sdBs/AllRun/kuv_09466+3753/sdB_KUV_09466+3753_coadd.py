from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.416333,37.651356],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_09466+3753/sdB_KUV_09466+3753_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_09466+3753/sdB_KUV_09466+3753_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
