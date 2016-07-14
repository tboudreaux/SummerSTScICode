from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.621417,26.007972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_174229.14+260028.7/sdB_sdssj_174229.14+260028.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_174229.14+260028.7/sdB_sdssj_174229.14+260028.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
