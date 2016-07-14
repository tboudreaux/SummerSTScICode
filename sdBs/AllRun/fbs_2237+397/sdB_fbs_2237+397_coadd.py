from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.846292,40.0015],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2237+397/sdB_fbs_2237+397_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2237+397/sdB_fbs_2237+397_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
