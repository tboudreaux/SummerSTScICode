from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[37.987958,44.956917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0228+447/sdB_fbs_0228+447_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0228+447/sdB_fbs_0228+447_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
