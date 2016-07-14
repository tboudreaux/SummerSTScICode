from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[354.548625,40.431361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2335+401/sdB_FBS_2335+401_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2335+401/sdB_FBS_2335+401_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
