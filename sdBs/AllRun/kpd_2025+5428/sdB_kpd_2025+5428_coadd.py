from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[306.823042,54.651008],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_2025+5428/sdB_kpd_2025+5428_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_2025+5428/sdB_kpd_2025+5428_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
