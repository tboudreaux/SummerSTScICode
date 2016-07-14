from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[36.092542,0.05375],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_022422.21+000313.5/sdB_SDSSJ_022422.21+000313.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_022422.21+000313.5/sdB_SDSSJ_022422.21+000313.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
