from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[143.49625,73.049222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0929+733/sdB_FBS_0929+733_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0929+733/sdB_FBS_0929+733_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
