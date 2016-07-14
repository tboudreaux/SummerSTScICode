from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[106.67625,41.589333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0703+416/sdB_fbs_0703+416_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0703+416/sdB_fbs_0703+416_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
