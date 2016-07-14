from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[149.728875,24.886611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_095854.93+245311.8/sdB_SDSSJ_095854.93+245311.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_095854.93+245311.8/sdB_SDSSJ_095854.93+245311.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
