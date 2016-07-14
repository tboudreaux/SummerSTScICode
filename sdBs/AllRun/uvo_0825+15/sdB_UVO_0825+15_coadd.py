from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[127.137417,14.867469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UVO_0825+15/sdB_UVO_0825+15_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UVO_0825+15/sdB_UVO_0825+15_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
