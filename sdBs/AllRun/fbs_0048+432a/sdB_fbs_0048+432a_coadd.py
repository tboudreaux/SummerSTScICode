from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[12.731875,43.561611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0048+432a/sdB_fbs_0048+432a_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0048+432a/sdB_fbs_0048+432a_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
