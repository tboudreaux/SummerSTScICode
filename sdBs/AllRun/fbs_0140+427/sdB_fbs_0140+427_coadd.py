from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[25.750333,42.9555],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0140+427/sdB_fbs_0140+427_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0140+427/sdB_fbs_0140+427_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
